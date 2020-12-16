package org.tensorflow.lite.examples.classification.main;

public class Food {
    public final static int FRENCH_FRIES = 0;
    public final static int HAMBURGER = 1;
    public final static int CAESAR_SALAD = 2;
    public final static int CHOCOLATE_CAKE = 3;
    public final static int PIZZA = 4;

    public static String name = "";
    public static String portion = "";
    public static int initPortion = 0;
    public static float calories = 0f;
    public static float totalFat = 0f;
    public static float saturatedFat = 0f;
    public static float cholesterol = 0f;
    public static float sodium = 0f;
    public static float carbohydrates = 0f;
    public static float proteins = 0f;

    public static void setData(String name, String portion, int initPortion, float calories,
                               float totalFat, float saturatedFat, float cholesterol, float sodium,
                               float carbohydrates, float proteins) {
        Food.name = name;
        Food.portion = portion;
        Food.initPortion = initPortion;
        Food.calories = calories;
        Food.totalFat = totalFat;
        Food.saturatedFat = saturatedFat;
        Food.cholesterol = cholesterol;
        Food.sodium = sodium;
        Food.carbohydrates = carbohydrates;
        Food.proteins = proteins;
    }

    public static void setFood(int id){
        switch (id){
            case FRENCH_FRIES:
                setData("Batata frita", "g", 100,  1.7f, 0.141f, 0.026f,
                        0.0004f, 0.0025f, 0.065f, 0.05f);
                break;
            case HAMBURGER:
                setData("Cheeseburger", "un", 1, 340f, 15f, 6f,
                        0.041f, 0.730f, 31f, 21f);
                break;
            case CAESAR_SALAD:
                setData("Salada Caesar", "g", 100,  1.7f, 0.141f, 0.026f,
                        0.0004f, 0.0025f, 0.065f, 0.05f);
                break;
            case CHOCOLATE_CAKE:
                setData("Bolo de chocolate", "fatia", 1, 297f, 13.6f, 5f,
                        0.064f, 0.812f, 31.7f, 11.4f);
                break;
            case PIZZA:
                setData("Pizza", "fatia", 1, 340f, 15f, 6f,
                        0.041f, 0.730f, 31f, 21f);
                break;
        }
    }
}
