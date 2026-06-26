from controller import Supervisor

robot = Supervisor()
time_step = 32

camera = robot.getDevice("camera")
if camera:
    camera.enable(time_step)
    camera.recognitionEnable(time_step)

feu_carrefour = robot.getFromDef("TRAFFIC_LIGHT")

while robot.step(time_step) != -1:
    nb_voitures = 0
    if camera:
        nb_voitures = len(camera.getRecognitionObjects())
        
    if nb_voitures > 2:
        if feu_carrefour:
            feu_carrefour.getField("state").setSFString("green")
    else:
        if feu_carrefour:
            feu_carrefour.getField("state").setSFString("red")
