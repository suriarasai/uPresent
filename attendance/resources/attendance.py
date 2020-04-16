from flask import Response, request
from flask_restful import Resource
from flask_restful_swagger import swagger
from flask import current_app
from database.models import Attendance
from resources.rekognition import compare_faces
from resources.geofence import validateVicinity
from resources.user import fetchUser
from resources.producer import publish_message


class AllAttendanceApi(Resource):

    @swagger.operation()
    def get(self):
        allAttendance = Attendance.objects().to_json()
        return Response(allAttendance, mimetype="application/json", status=200)

    @swagger.operation()
    def post(self):
        try:
            body = request.get_json()
            attendance = Attendance(**body)
            validateVicinity(body)
            user = fetchUser(attendance.username)
            compare_faces(attendance.capturedImageId, user.get('imageId')[0])
            if current_app.config['DATABASE_ENABLED'] == 1:
                attendance.save()
            publish_message(body)
        except Exception as ex:
            return {'message': str(ex)}, 400
        return {'id': str(attendance.id)}, 200


class AttendanceApi(Resource):

    @swagger.operation()
    def put(self, id):
        body = request.get_json()
        Attendance.objects.get(id=id).update(**body)
        return '', 200

    @swagger.operation()
    def delete(self, id):
        movie = Attendance.objects.get(id=id).delete()
        return '', 200

    @swagger.operation()
    def get(self, id):
        attendance = Attendance.objects.get(userId=id).to_json()
        return Response(attendance, mimetype="application/json", status=200)
