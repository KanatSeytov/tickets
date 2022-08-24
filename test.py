import unittest
import app

class ImageTest(unittest.TestCase):

    def testPdfToImg(self):
        pdf_tickets = app.tickets
        tickets = app.pdf_to_jpg(pdf_tickets)
        for ticket in tickets:
            self.assertEqual(ticket[0:4], 'Page')

    def testImageToText(self):
        tickets = app.pdf_to_jpg(app.tickets)
        for ticket in tickets:
            image = app.openImage(ticket)
            self.assertEqual(app.normilize_image(image).shape[1],2893)
            self.assertEqual(app.normilize_image(image).shape[0],4094)
    
    def testGetUser(self):
        tickets = app.pdf_to_jpg(app.tickets)
        for ticket in tickets:
            image = app.openImage(ticket)
            image = app.normilize_image(image)

            user_name = app.get_useraname_from_image(image)
            user_name = app.transform_image_to_text(user_name)

            self.assertEqual(len(user_name), 2)
    
    def testGetDate(self):
        tickets = app.pdf_to_jpg(app.tickets)
        for ticket in tickets:
            image = app.openImage(ticket)
            image = app.normilize_image(image)

            travel_date = app.get_travel_date_from_image(image)
            travel_date = app.transform_image_to_text(travel_date)

            self.assertEqual(len(travel_date), 3)

unittest.main()