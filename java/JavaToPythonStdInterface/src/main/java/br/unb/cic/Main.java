package br.unb.cic;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Objects;

/**
 * Hello world!
 *
 */
public class Main
{
    public static void main( String[] args ) throws IOException {
        if (args.length < 4) {
            System.out.println("Expected: java -jar file.jar STDIN|NATIVE config_path dataset_path output_path python_path (if applicable)");
            System.exit(1);
        }

        String configPath = args[1];
        String datasetPath = args[2];
        String outputPath = args[3];
        System.out.println(configPath);
        System.out.println(datasetPath);
        System.out.println(outputPath);
        Dataset dataset = Utils.readDataset(datasetPath);
        System.out.println(dataset.warm_up.size());
        System.out.println(dataset.data.size());

        if (Objects.equals(args[0], "STDIN")) {
            if (args.length < 5) {
                System.out.println("Expected: java -jar file.jar STDIN|NATIVE config_path dataset_path output_path python_path (if applicable)");
                System.exit(1);
            }
            String pythonPath = args[4];
            StdInterface.Run(dataset, configPath, outputPath, pythonPath);
        } else if (Objects.equals(args[0], "NATIVE")) {
            System.out.println("ok");
        } else {
            throw new Error("Not supported");
        }
    }
}
