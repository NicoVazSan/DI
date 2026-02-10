package com.example.aula.ui;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;

import com.example.aula.R;
import com.example.aula.data.AuthRepository;
import com.example.aula.data.InMemoryNoticeRepository;
import com.example.aula.viewmodel.AuthViewModel;
import com.example.aula.viewmodel.AuthViewModelFactory;
import com.example.aula.viewmodel.ProfileViewModel;
import com.example.aula.viewmodel.NoticeViewModelFactory;
import com.example.aula.viewmodel.SettingsViewModel;
import com.example.aula.viewmodel.SettingsViewModelFactory;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.materialswitch.MaterialSwitch;
import com.google.android.material.textfield.TextInputLayout;
import com.google.firebase.auth.FirebaseAuth;



public class ProfileFragment extends Fragment {

    public ProfileFragment() {
        super(R.layout.fragment_profile);
    }

    private AuthViewModel vm;

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {


        MaterialButton btnLogout = view.findViewById(R.id.btnLogout);

        TextView UID = view.findViewById(R.id.UID);


        MaterialSwitch switchDark = view.findViewById(R.id.switchDarkMode);

        SettingsViewModelFactory settingsFactory = new SettingsViewModelFactory(requireContext());
        SettingsViewModel settingsVm = new ViewModelProvider(this, settingsFactory)
                .get(SettingsViewModel.class);


        settingsVm.getDarkMode().observe(getViewLifecycleOwner(), enabled -> {
            if (enabled == null) return;

            if (switchDark.isChecked() != enabled) {
                switchDark.setChecked(enabled);
            }

            AppCompatDelegate.setDefaultNightMode(
                    enabled ? AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO
            );
        });

        switchDark.setOnCheckedChangeListener((buttonView, isChecked) -> {
            settingsVm.setDarkMode(isChecked);
        });

        AuthRepository repo = new AuthRepository();
        AuthViewModelFactory factory = new AuthViewModelFactory(repo);
        vm = new ViewModelProvider(requireActivity(), factory).get(AuthViewModel.class);

        UID.append(vm.getUID());

        btnLogout.setOnClickListener(v -> {
            FirebaseAuth.getInstance().signOut();
            NavHostFragment.findNavController(this)
                    .navigate(R.id.action_ProfileFragment_to_loginFragment);
        });
    }
}