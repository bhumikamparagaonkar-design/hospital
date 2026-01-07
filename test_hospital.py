from hospital import hospital_details


def test_hospital_details():
    expected_output = (
        "Hospital ID    : H101\n"
        "Hospital Name  : City Care Hospital\n"
        "Location       : Hyderabad\n"
        "Available Beds : 120\n"
    )

    assert hospital_details(
        "H101", "City Care Hospital", "Hyderabad", 120
    ) == expected_output
