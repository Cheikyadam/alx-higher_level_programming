#!/usr/bin/python3
"""
Load, add, save"""
import sys
import os


def est_fichier_vide(nom_fichier):
    """To check if a file is empty or not"""
    try:
        return os.path.getsize(nom_fichier) == 0
    except FileNotFoundError:
        return True


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
Lis = []
if not est_fichier_vide("add_item.json"):
    Lis = load_from_json_file("add_item.json")

for i in range(1, len(sys.argv)):
    Lis.append(sys.argv[i])
save_to_json_file(Lis, "add_item.json")
