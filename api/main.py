from flask import Flask, request, jsonify
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('results.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_result():
    roll_number = request.args.get('rollNumber')  # Match the URL parameter name
    examination = request.args.get('examination')
    regulation = request.args.get('regulation')

    if not roll_number or not examination or not regulation:
        return jsonify({'error': 'Roll number, examination, and regulation are required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT roll_number, polytechnic_name, city, type, publish_date, referred_subjects, referred_p, referred_t, semester, examination, regulation, GPA, grade
        FROM semester01_4th_2022
        WHERE roll_number = ? AND examination = ? AND regulation = ?
    ''', (roll_number, examination, regulation))
    result1 = cursor.fetchone()

    cursor.execute('''
        SELECT roll_number, polytechnic_name, city, type, publish_date, referred_subjects, referred_p, referred_t, semester, examination, regulation, GPA, grade
        FROM semester02_2nd_2022
        WHERE roll_number = ? AND examination = ? AND regulation = ?
    ''', (roll_number, examination, regulation))
    result2 = cursor.fetchone()

    results = []
    if result1:
        results.append({
            'roll_number': result1['roll_number'],
            'polytechnic_name': result1['polytechnic_name'],
            'city': result1['city'],
            'type': result1['type'],
            'publish_date': result1['publish_date'],
            'referred_subjects': result1['referred_subjects'],
            'referred_p': result1['referred_p'],
            'referred_t': result1['referred_t'],
            'semester': result1['semester'],
            'examination': result1['examination'],
            'regulation': result1['regulation'],
            'GPA': result1['GPA'],
            'grade': result1['grade']
        })
    if result2:
        results.append({
            'roll_number': result2['roll_number'],
            'polytechnic_name': result2['polytechnic_name'],
            'city': result2['city'],
            'type': result2['type'],
            'publish_date': result2['publish_date'],
            'referred_subjects': result2['referred_subjects'],
            'referred_p': result2['referred_p'],
            'referred_t': result2['referred_t'],
            'semester': result2['semester'],
            'examination': result2['examination'],
            'regulation': result2['regulation'],
            'GPA': result2['GPA'],
            'grade': result2['grade']
        })

    conn.close()

    if results:
        return jsonify(results)
    else:
        return jsonify({'error': 'No grades found for the specified criteria'}), 404
