package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import androidx.fragment.app.Fragment;

public class CatalogFragment extends Fragment {

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_catalog, container, false);

        Button btnDetail = view.findViewById(R.id.btnOpenDetail);
        Button btnCatalog = view.findViewById(R.id.btnOpenCatalog);

        // Abrir DetailActivity
        btnDetail.setOnClickListener(v -> {
            Intent intent = new Intent(getActivity(), Detail_activity.class);
            startActivity(intent);
        });

        // Abrir CatalogActivity
        btnCatalog.setOnClickListener(v -> {
            Intent intent = new Intent(getActivity(), CatalogActivity.class);
            startActivity(intent);
        });

        return view;
    }
}