#!/usr/bin/python3
"""
This code is used as an example
"""
from functools import wraps
from flask import Flask, request, jsonify

app=Flask(__name__)

def check_card(card_name):
    """
    This function validates credit card transactions
    """
    wraps(card_name)
    def validation(*args, **kwargs):
        """
    This function is a decorator
    """
        data=request.get_json()
        if not data.get("status"):
            response={"approved":False,
            "newLimit":data.get("limit"),
            "reason":"Blocked card"}
            return jsonify(response)
        if data.get("limit") < data.get("transaction").get("amoount"):
            response={"approved":False,
            "newLimit":data.get("limit"),
            "reason":"Transaction above limit"}
            return jsonify(response)
        return card_name(*args, **kwargs)
    return validation

@app.route("/api/transaction",methods=["POST"])
@check_card

def transaction():
    """
    This function is responsible for exposing the endpoint for receiving requests
    """
    card = request.get_json()
    new_limit = card.get("limit")- card.get("transaction").get("amoount")
    response={"approved":True,"newLimit":new_limit}
    return jsonify(response)

if __name__ =='__main__':
    app.run(debug=True)
