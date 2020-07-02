package br.unb.cic;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class StdInterface {

    private static Logger logger = Logger.getGlobal();

    public static void Run(Dataset dataset, String configPath, String outputPath, String pythonPath) throws IOException {
        ProcessBuilder builder = new ProcessBuilder("python3", pythonPath, configPath);
        Process process = builder.start();
        BufferedWriter p_stdin = new BufferedWriter(new OutputStreamWriter(process.getOutputStream()));
        BufferedReader p_stdout = new BufferedReader(new InputStreamReader(process.getInputStream()));
        BufferedReader p_stderr = new BufferedReader(new InputStreamReader(process.getErrorStream()));

        RunInfo runInfo = new RunInfo();
        runInfo.name = "Java Python Interface Run - Hot loop in Java communicating with Python";
        runInfo.results = new ArrayList<>();
        runInfo.warm_up_results = new ArrayList<>();

        logger.info(String.format("Waiting for program to be ready"));
        while (!p_stdout.ready()) {
            if (p_stderr.ready()) {
                Logger.getGlobal().warning(p_stderr.readLine());
            }
        };

        String firstLine = p_stdout.readLine();
        if (!firstLine.equals("READY")) {
            throw new IOException(firstLine);
        }

        // warmup

        for (List<Double> seq : dataset.warm_up) {

            long startTime = System.nanoTime();

            StringBuilder sBuilder = new StringBuilder();
            for (int j = 0; j < seq.size(); j++) {
                if (j != 0)
                    sBuilder.append(' ');
                sBuilder.append(seq.get(j));
            }
            writeStdin(sBuilder.toString(), p_stdin);
            String line = p_stdout.readLine();
            Integer result = Integer.parseInt(line);

            Long stopTime = System.nanoTime();

            Result res = new Result();
            res.input = seq;
            res.duration = (int)(stopTime - startTime);
            res.output = result;
            runInfo.warm_up_results.add(res);
        }

        for (List<Double> seq : dataset.data) {

            long startTime = System.nanoTime();

            StringBuilder sBuilder = new StringBuilder();
            for (int j = 0; j < seq.size(); j++) {
                if (j != 0)
                    sBuilder.append(' ');
                sBuilder.append(seq.get(j));
            }
            writeStdin(sBuilder.toString(), p_stdin);
            String line = p_stdout.readLine();
            Integer result = Integer.parseInt(line);

            Long stopTime = System.nanoTime();

            Result res = new Result();
            res.input = seq;
            res.duration = (int)((stopTime - startTime) / 1000);
            res.output = result;
            runInfo.results.add(res);
        }

        logger.info("Finished");
        logger.info(runInfo.name);
        Utils.writeDataset(outputPath, "java-python-interface.json", runInfo);
    }

    static private void writeStdin(String text, BufferedWriter p_stdin) throws IOException {
        p_stdin.write(text);
        p_stdin.newLine();
        p_stdin.flush();
    }
}
