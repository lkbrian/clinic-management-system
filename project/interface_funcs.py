# # interface_func(s).py
# import click
# from interface import consecutive_registration_action


# @click.command()
# @click.option("--name", prompt="Enter Child's Fullname: ")
# @click.option("--cert_no", prompt="Enter Child's Certificate/Notification Number: ", type=int)
# @click.option("--d_o_b", prompt="Enter child's Date of Birth (YYYY-MM-DD): ")
# @click.option("--parent_id", prompt="Enter the Parent's National ID Number: ", type=int)
# def register_child(name, cert_no, d_o_b, parent_id):
#     try:
#         Child.add_child(name, cert_no, d_o_b, parent_id)
#         click.echo("Child registered successfully.")
#         consecutive_registration_action()

#     except Exception as error:
#         click.echo("Error during child registration: ", error)

# @click.command()
# @click.option("--father", prompt="Enter Father's Fullname: ")
# @click.option("--mother", prompt="Enter Mother's Fullname: ")
# @click.option("--national_id", prompt="Enter the point parent's National ID Number: ", type=int)
# def register_parent(father, mother, national_id):
#     try:
#         Parent.add_parent(father, mother, national_id)
#         click.echo("Parent registered successfully.")
#         consecutive_registration_action()

#     except Exception as error:
#         click.echo("Error during parent registration: ", error)

# @click.command()
# @click.option("--child_name", prompt="Enter Child's Fullname: ")
# @click.option("--parent_name", prompt="Enter Parent's Fullname: ")
# @click.option("--vaccine", prompt="Enter Vaccine: ")
# @click.option("--status", prompt="Enter Status: ")
# @click.option("--doctor", prompt="Enter Doctor in Charge: ")
# @click.option("--appointment_date", prompt="Enter Appointment Date (YYYY-MM-DD): ")
# def register_appointment(child_name, parent_name, vaccine, status, doctor, appointment_date):
#     try:
#         Appointment.set_appointment(child_name, parent_name, vaccine, status, doctor, appointment_date)
#         click.echo("Appointment set successfully.")
#     except Exception as error:
#         click.echo("Error during appointment setting: ", error)









# # def consecutive_registration_action():
# #     click.echo("\nProceed to: ")
# #     click.echo("\n1. Registration menu")
# #     click.echo("2. Main menu")
# #     choice = click.prompt("Select a choice", type=int)

# #     if choice == 1:
# #         Registration()
# #     else:
# #         main()
