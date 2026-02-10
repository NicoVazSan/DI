package com.example.aula.viewmodel;

import androidx.annotation.NonNull;
import androidx.lifecycle.ViewModel;
import androidx.lifecycle.ViewModelProvider;

import com.example.aula.data.AuthRepository;
import com.example.aula.data.InMemoryNoticeRepository;

public class ProfileViewModelFactory implements ViewModelProvider.Factory {

    private final AuthRepository repo;
    public ProfileViewModelFactory(AuthRepository repo) {
        this.repo = repo;
    }

    @NonNull
    public <T extends ViewModel> T create(@NonNull Class<T> modelClass) {
        if (modelClass.isAssignableFrom(ProfileViewModel.class)) {
            return (T) new ProfileViewModel(repo);
        }
        throw new IllegalArgumentException("Unknown ViewModel class");
    }
}
