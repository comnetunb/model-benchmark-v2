package br.unb.cic;

import com.google.gson.Gson;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Paths;

public class Utils {
    public static Dataset readDataset(String path) throws FileNotFoundException {
        Gson gson= new Gson();
        return gson.fromJson(new FileReader(path), Dataset.class);
    }

    public static void writeDataset(String path, String name, RunInfo info) throws IOException {
        Gson gson= new Gson();
        FileWriter writer = new FileWriter(Paths.get(path, name).toString());
        gson.toJson(info,writer);
        writer.flush();
        writer.close();
    }
}
