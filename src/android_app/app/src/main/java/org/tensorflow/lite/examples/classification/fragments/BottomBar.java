package org.tensorflow.lite.examples.classification.fragments;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.fragment.app.Fragment;

import org.tensorflow.lite.examples.classification.main.ClassifierActivity;
import org.tensorflow.lite.examples.classification.main.MainActivity;
import org.tensorflow.lite.examples.classification.R;
import org.tensorflow.lite.examples.classification.activities.PopularActivity;


/**
 * A simple {@link Fragment} subclass.
 * Use the {@link BottomBar#newInstance} factory method to
 * create an instance of this fragment.
 */
public class BottomBar extends Fragment {
    // TODO: Rename parameter arguments, choose names that match
    // the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
    private static final String ARG_PARAM1 = "param1";
    private static final String ARG_PARAM2 = "param2";

    // TODO: Rename and change types of parameters
    private String mParam1;
    private String mParam2;

    public BottomBar() {
        // Required empty public constructor
    }

    /**
     * Use this factory method to create a new instance of
     * this fragment using the provided parameters.
     *
     * @param param1 Parameter 1.
     * @param param2 Parameter 2.
     * @return A new instance of fragment BottomBar.
     */
    // TODO: Rename and change types and number of parameters
    public static BottomBar newInstance(String param1, String param2) {
        BottomBar fragment = new BottomBar();
        Bundle args = new Bundle();
        args.putString(ARG_PARAM1, param1);
        args.putString(ARG_PARAM2, param2);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            mParam1 = getArguments().getString(ARG_PARAM1);
            mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_bottom_bar, container, false);

        Button btnHome = v.findViewById(R.id.btnHome);
        Button btnPopular = v.findViewById(R.id.btnMain);
        Button btnScan = v.findViewById(R.id.btnPhoto);

        btnHome.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(v.getContext(), MainActivity.class));
            }
        });

        btnPopular.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(v.getContext(), PopularActivity.class));
            }
        });

        btnScan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(v.getContext(), ClassifierActivity.class));
            }
        });

        return v;
    }
}
