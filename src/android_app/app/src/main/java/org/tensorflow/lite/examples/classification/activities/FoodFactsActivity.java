package org.tensorflow.lite.examples.classification.activities;

import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import org.tensorflow.lite.examples.classification.main.Food;
import org.tensorflow.lite.examples.classification.R;

public class FoodFactsActivity extends AppCompatActivity {

    private TextView foodName;
    private EditText portionNum;
    private TextView foodPortion;
    private TextView portionSizeTitle;
    private TextView calories;
    private TextView totalFat;
    private TextView saturatedFat;
    private TextView cholesterol;
    private TextView carbohydrates;
    private TextView proteins;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_food_facts);

        foodName = findViewById(R.id.tvFoodName);
        portionNum = findViewById(R.id.etxtPortionNum);
        foodPortion = findViewById(R.id.tvFoodPortion);
        portionSizeTitle = findViewById(R.id.tvPortionSizeTitle);
        calories = findViewById(R.id.tvCalories);
        totalFat = findViewById(R.id.tvTotalFat);
        saturatedFat = findViewById(R.id.tvSaturatedFat);
        cholesterol = findViewById(R.id.tvCholesterol);
        carbohydrates = findViewById(R.id.tvCarbohydrates);
        proteins = findViewById(R.id.tvProteins);

        foodName.setText(Food.name);
        portionNum.setText(Integer.toString(Food.initPortion));
        foodPortion.setText(Food.portion);
        portionSizeTitle.setText("Tamanho da porção ".concat(Integer.toString(Food.initPortion)).concat(" ").concat(Food.portion));
        calories.setText(Integer.toString((int)(Food.initPortion * Food.calories)));
        totalFat.setText(Float.toString(Food.initPortion * Food.totalFat));
        saturatedFat.setText(Float.toString(Food.initPortion * Food.saturatedFat));
        cholesterol.setText(Float.toString(Food.initPortion * Food.cholesterol));
        carbohydrates.setText(Float.toString(Food.initPortion * Food.carbohydrates));
        proteins.setText(Float.toString(Food.initPortion * Food.proteins));
    }
}
