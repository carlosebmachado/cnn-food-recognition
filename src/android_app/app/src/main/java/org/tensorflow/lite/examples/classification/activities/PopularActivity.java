package org.tensorflow.lite.examples.classification.activities;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import org.tensorflow.lite.examples.classification.main.Food;
import org.tensorflow.lite.examples.classification.R;

public class PopularActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_popular);
    }

    public void card1(View v){
        Food.setFood(Food.FRENCH_FRIES);
        startActivity(new Intent(v.getContext(), FoodFactsActivity.class));
    }

    public void card2(View v){
        Food.setFood(Food.CAESAR_SALAD);
        startActivity(new Intent(v.getContext(), FoodFactsActivity.class));
    }

    public void card3(View v){
        Food.setFood(Food.CHOCOLATE_CAKE);
        startActivity(new Intent(v.getContext(), FoodFactsActivity.class));
    }

    public void card4(View v){
        Food.setFood(Food.HAMBURGER);
        startActivity(new Intent(v.getContext(), FoodFactsActivity.class));
    }

    public void card5(View v){
        Food.setFood(Food.PIZZA);
        startActivity(new Intent(v.getContext(), FoodFactsActivity.class));
    }
}
