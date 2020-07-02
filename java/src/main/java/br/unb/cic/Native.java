package br.unb.cic;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class Native {
    private static Logger logger = Logger.getGlobal();

    public static void Run(Dataset dataset, String configPath, String outputPath) throws Exception {
        Classifier classifier = new Classifier(configPath);
        RunInfo runInfo = new RunInfo();
        runInfo.name = "Java Native Run - Hot loop in Java";
        runInfo.results = new ArrayList<>();
        runInfo.warm_up_results = new ArrayList<>();
        // warmup

        for (List<Double> seq : dataset.warm_up) {

            long startTime = System.nanoTime();

            double[] arr = new double[seq.size()];
            for (int i = 0; i < seq.size(); i++) arr[i] = seq.get(i);
            Integer result = classifier.classify(arr);

            Long stopTime = System.nanoTime();

            Result res = new Result();
            res.input = seq;
            res.duration = (int)(stopTime - startTime);
            res.output = result;
            runInfo.warm_up_results.add(res);
        }

        for (List<Double> seq : dataset.data) {

            long startTime = System.nanoTime();

            double[] arr = new double[seq.size()];
            for (int i = 0; i < seq.size(); i++) arr[i] = seq.get(i);
            Integer result = classifier.classify(arr);

            Long stopTime = System.nanoTime();

            Result res = new Result();
            res.input = seq;
            res.duration = (int)((stopTime - startTime) / 1000);
            res.output = result;
            runInfo.results.add(res);
        }

        logger.info("Finished");
        logger.info(runInfo.name);
        Utils.writeDataset(outputPath, "java-native.json", runInfo);
    }
}
