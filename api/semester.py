from flask import Flask, request, jsonify
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('results.db')
    conn.row_factory = sqlite3.Row
    return conn

#1st semester result
def get_1st():
    roll_number = request.args.get('rollNumber')  # Update to match the URL parameter name
    print(f"Received roll number: {roll_number}")  # Debugging statement
    if not roll_number:
        return jsonify({'error': 'Roll number is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Query both tables separately
    cursor.execute('''
        SELECT roll_number,semester, GPA, grade
        FROM semester01_1st_2022
        WHERE roll_number = ?
    ''', (roll_number,))
    result1 = cursor.fetchone()

    cursor.execute('''
        SELECT roll_number,semester, GPA, grade
        FROM semester02_1st_2022
        WHERE roll_number = ?
    ''', (roll_number,))
    result2 = cursor.fetchone()

    conn.close()

    # Combine results
    results = []
    if result1:
        results.append({
            'roll_number': result1['roll_number'],
            'semester': result1['semester'],
            'GPA': result1['GPA'],
            'grade': result1['grade']
        })
    if result2:
        results.append({
            'roll_number': result2['roll_number'],
            'semester': result2['semester'],
            'GPA': result2['GPA'],
            'grade': result2['grade']
        })

    if results:
        return jsonify(results)
    else:
        return jsonify({'error': 'No grades found for the specified semester'}), 404




#2nd semester result
def get_2nd():
    roll_number = request.args.get('rollNumber')  # Update to match the URL parameter name
    print(f"Received roll number: {roll_number}")  # Debugging statement
    if not roll_number:
        return jsonify({'error': 'Roll number is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Query both tables separately
    cursor.execute('''
        SELECT roll_number,semester, GPA, grade
        FROM semester01_2nd_2022
        WHERE roll_number = ?
    ''', (roll_number,))
    result1 = cursor.fetchone()

    cursor.execute('''
        SELECT roll_number,semester, GPA, grade
        FROM semester02_2nd_2022
        WHERE roll_number = ?
    ''', (roll_number,))
    result2 = cursor.fetchone()

    conn.close()

    # Combine results
    results = []
    if result1:
        results.append({
            'roll_number': result1['roll_number'],
            'semester': result1['semester'],
            'GPA': result1['GPA'],
            'grade': result1['grade']
        })
    if result2:
        results.append({
            'roll_number': result2['roll_number'],
            'semester': result2['semester'],
            'GPA': result2['GPA'],
            'grade': result2['grade']
        })

    if results:
        return jsonify(results)
    else:
        return jsonify({'error': 'No grades found for the specified semester'}), 404



#3rd semester result
def get_3rd():
    roll_number = request.args.get('rollNumber')  # Update to match the URL parameter name
    print(f"Received roll number: {roll_number}")  # Debugging statement
    if not roll_number:
        return jsonify({'error': 'Roll number is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Query both tables separately
    cursor.execute('''
        SELECT roll_number,semester, GPA, grade
        FROM semester01_3th_2022
        WHERE roll_number = ?
    ''', (roll_number,))
    result1 = cursor.fetchone()

    # cursor.execute('''
    #     SELECT roll_number,semester, GPA, grade
    #     FROM semester02_1st_2022
    #     WHERE roll_number = ?
    # ''', (roll_number,))
    # result2 = cursor.fetchone()

    conn.close()

    # Combine results
    results = []
    if result1:
        results.append({
            'roll_number': result1['roll_number'],
            'semester': result1['semester'],
            'GPA': result1['GPA'],
            'grade': result1['grade']
        })
    # if result2:
    #     results.append({
    #         'roll_number': result2['roll_number'],
    #         'semester': result2['semester'],
    #         'GPA': result2['GPA'],
    #         'grade': result2['grade']
    #     })

    if results:
        return jsonify(results)
    else:
        return jsonify({'error': 'No grades found for the specified semester'}), 404


#4th semester result
def get_4th():
    roll_number = request.args.get('rollNumber')  # Update to match the URL parameter name
    print(f"Received roll number: {roll_number}")  # Debugging statement
    if not roll_number:
        return jsonify({'error': 'Roll number is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Query both tables separately
    cursor.execute('''
        SELECT roll_number,semester, GPA, grade
        FROM semester01_4th_2022
        WHERE roll_number = ?
    ''', (roll_number,))
    result1 = cursor.fetchone()

    # cursor.execute('''
    #     SELECT roll_number,semester, GPA, grade
    #     FROM semester02_1st_2022
    #     WHERE roll_number = ?
    # ''', (roll_number,))
    # result2 = cursor.fetchone()

    conn.close()

    # Combine results
    results = []
    if result1:
        results.append({
            'roll_number': result1['roll_number'],
            'semester': result1['semester'],
            'GPA': result1['GPA'],
            'grade': result1['grade']
        })
    # if result2:
    #     results.append({
    #         'roll_number': result2['roll_number'],
    #         'semester': result2['semester'],
    #         'GPA': result2['GPA'],
    #         'grade': result2['grade']
    #     })

    if results:
        return jsonify(results)
    else:
        return jsonify({'error': 'No grades found for the specified semester'}), 404


#next semester


# @app.route('/1st', methods=['GET'])
# def get_1st():
#     roll_number = request.args.get('rollNumber')  # Update to match the URL parameter name
#     print(f"Received roll number: {roll_number}")  # Debugging statement
#     if not roll_number:
#         return jsonify({'error': 'Roll number is required'}), 400
#
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     # Query both tables separately
#     cursor.execute('''
#         SELECT roll_number,semester, GPA, grade
#         FROM semester01_1st_2022
#         WHERE roll_number = ?
#     ''', (roll_number,))
#     result1 = cursor.fetchone()
#
#     cursor.execute('''
#         SELECT roll_number,semester, GPA, grade
#         FROM semester02_1st_2022
#         WHERE roll_number = ?
#     ''', (roll_number,))
#     result2 = cursor.fetchone()
#
#     conn.close()
#
#     # Combine results
#     results = []
#     if result1:
#         results.append({
#             'roll_number': result1['roll_number'],
#             'semester': result1['semester'],
#             'GPA': result1['GPA'],
#             'grade': result1['grade']
#         })
#     if result2:
#         results.append({
#             'roll_number': result2['roll_number'],
#             'semester': result2['semester'],
#             'GPA': result2['GPA'],
#             'grade': result2['grade']
#         })
#
#     if results:
#         return jsonify(results)
#     else:
#         return jsonify({'error': 'No grades found for the specified semester'}), 404
#
#
# @app.route('/2nd', methods=['GET'])
# def get_2nd():
#     roll_number = request.args.get('rollNumber')  # Update to match the URL parameter name
#     print(f"Received roll number: {roll_number}")  # Debugging statement
#     if not roll_number:
#         return jsonify({'error': 'Roll number is required'}), 400
#
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     # Query both tables separately
#     cursor.execute('''
#         SELECT roll_number,semester, GPA, grade
#         FROM semester01_2nd_2022
#         WHERE roll_number = ?
#     ''', (roll_number,))
#     result1 = cursor.fetchone()
#
#     cursor.execute('''
#         SELECT roll_number,semester, GPA, grade
#         FROM semester02_2nd_2022
#         WHERE roll_number = ?
#     ''', (roll_number,))
#     result2 = cursor.fetchone()
#
#     conn.close()
#
#     # Combine results
#     results = []
#     if result1:
#         results.append({
#             'roll_number': result1['roll_number'],
#             'semester': result1['semester'],
#             'GPA': result1['GPA'],
#             'grade': result1['grade']
#         })
#     if result2:
#         results.append({
#             'roll_number': result2['roll_number'],
#             'semester': result2['semester'],
#             'GPA': result2['GPA'],
#             'grade': result2['grade']
#         })
#
#     if results:
#         return jsonify(results)
#     else:
#         return jsonify({'error': 'No grades found for the specified semester'}), 404
#
#
# @app.route('/3th', methods=['GET'])
# def get_3th():
#     roll_number = request.args.get('rollNumber')  # Update to match the URL parameter name
#     print(f"Received roll number: {roll_number}")  # Debugging statement
#     if not roll_number:
#         return jsonify({'error': 'Roll number is required'}), 400
#
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     # Query both tables separately
#     cursor.execute('''
#         SELECT roll_number,semester, GPA, grade
#         FROM semester01_3th_2022
#         WHERE roll_number = ?
#     ''', (roll_number,))
#     result1 = cursor.fetchone()
#
#     # cursor.execute('''
#     #     SELECT roll_number,semester, GPA, grade
#     #     FROM semester02_1st_2022
#     #     WHERE roll_number = ?
#     # ''', (roll_number,))
#     # result2 = cursor.fetchone()
#
#     conn.close()
#
#     # Combine results
#     results = []
#     if result1:
#         results.append({
#             'roll_number': result1['roll_number'],
#             'semester': result1['semester'],
#             'GPA': result1['GPA'],
#             'grade': result1['grade']
#         })
#     # if result2:
#     #     results.append({
#     #         'roll_number': result2['roll_number'],
#     #         'semester': result2['semester'],
#     #         'GPA': result2['GPA'],
#     #         'grade': result2['grade']
#     #     })
#
#     if results:
#         return jsonify(results)
#     else:
#         return jsonify({'error': 'No grades found for the specified semester'}), 404
#
#
# @app.route('/4th', methods=['GET'])
# def get_4th():
#     roll_number = request.args.get('rollNumber')  # Update to match the URL parameter name
#     print(f"Received roll number: {roll_number}")  # Debugging statement
#     if not roll_number:
#         return jsonify({'error': 'Roll number is required'}), 400
#
#     conn = get_db_connection()
#     cursor = conn.cursor()
#
#     # Query both tables separately
#     cursor.execute('''
#         SELECT roll_number,semester, GPA, grade
#         FROM semester01_4th_2022
#         WHERE roll_number = ?
#     ''', (roll_number,))
#     result1 = cursor.fetchone()
#
#     # cursor.execute('''
#     #     SELECT roll_number,semester, GPA, grade
#     #     FROM semester02_1st_2022
#     #     WHERE roll_number = ?
#     # ''', (roll_number,))
#     # result2 = cursor.fetchone()
#
#     conn.close()
#
#     # Combine results
#     results = []
#     if result1:
#         results.append({
#             'roll_number': result1['roll_number'],
#             'semester': result1['semester'],
#             'GPA': result1['GPA'],
#             'grade': result1['grade']
#         })
#     # if result2:
#     #     results.append({
#     #         'roll_number': result2['roll_number'],
#     #         'semester': result2['semester'],
#     #         'GPA': result2['GPA'],
#     #         'grade': result2['grade']
#     #     })
#
#     if results:
#         return jsonify(results)
#     else:
#         return jsonify({'error': 'No grades found for the specified semester'}), 404
