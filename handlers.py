import webapp2
import enter

app = webapp2.WSGIApplication([('/', enter.EnterPage)],debug=True)
