import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime


@anvil.server.callable
def add_feedback(name, email, feedback):
  # This function is called from HomeForm when the user clicks "SUBMIT".

  # We use Anvil's built-in Data Tables to save the feedback.
  # You can find your Data Tables in the navigation on the left.
  app_tables.feedback.add_row(
    name=name, email=email, feedback=feedback, created=datetime.now()
  )

  # Now we send an email to you, the app's author!
  anvil.email.send(  # to="somebody@example.com", # Change this to your email address
    subject="Feedback from {}".format(name),
    text="""
    A new person has filled out the feedback form!
    
    Name: {}
    Email address: {}
    Feedback:
    {}
    """.format(name, email, feedback),
  )

  # Pretty simple, huh?
  # To learn more about Anvil, go to:
  # https://anvil.works/learn/tutorials
