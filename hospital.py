def hospital_details(hospital_id, name, location, beds):
    result = (
        f"Hospital ID    : {hospital_id}\n"
        f"Hospital Name  : {name}\n"
        f"Location       : {location}\n"
        f"Available Beds : {beds}\n"
    )
    return result


if __name__ == "__main__":
    hospital_id = "H101"
    name = "City Care Hospital"
    location = "Hyderabad"
    beds = 120

    print(hospital_details(hospital_id, name, location, beds))
