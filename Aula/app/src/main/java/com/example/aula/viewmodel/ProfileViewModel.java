package com.example.aula.viewmodel;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.aula.data.AuthRepository;
import com.example.aula.data.InMemoryNoticeRepository;

import java.util.List;

public class ProfileViewModel extends ViewModel {

    private final AuthRepository repo;

    private String _UID = " ";

    public ProfileViewModel(AuthRepository repo) {
        this.repo = repo;
    }


    public String getUID() {

        _UID = repo.getUID();

        return _UID; }




}