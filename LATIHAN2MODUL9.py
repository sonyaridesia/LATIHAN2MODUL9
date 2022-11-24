#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 20:02:14 2022

@author: sonyaridesia
"""

def make_file():
    file = open ("Praktikum_9_Latihan_2.txt", "w")
    nama = str(input("Masukan nama anda: "))
    nim = str(input("Masukan NIM anda: "))
    angkatan = str(input("Masukan tahun angkatan anda: "))
    file.write("Nama: " + nama)
    file.write("\nNIM: " + nim)
    file.write("\nAngkatan: " + angkatan)
    file.close()

def read_file():
    file = open("Praktikum_9_Latihan_2.txt", "r")
    text = file.read()
    print(text)
    file.close()

def add_file():
    file = open("Praktikum_9_Latihan_2.txt", "a")
    friend = str(input ("Masukan nama sahabat anda: "))
    note = input("Masukan catatan anda: ")
    file.write("\nSahabat: " + friend)
    file.write("\nCatatan: " + note)
    file.close()

def panggil_file():
    ulang = True
    while(ulang):
        print("### Program File Handling ###")
        print("1. Membuat & Menulis File")
        print("2. Membaca File")
        print("3. Menambahkan Isi File")
        print("4. Keluar dari Program")
        choose = int(input("Masukan Nomor Pilihan Anda: "))
        
        if (choose == 1):
            print("\n")
            make_file()
            print("\n")
            
        if (choose == 2):
            print("\n")
            read_file()
            print("\n")
            
        if (choose == 3):
            print("\n")
            add_file()
            print("\n")
            
        if (choose == 4):
            print("Terimakasih telah menggunakan program")
            ulang = False

panggil_file()