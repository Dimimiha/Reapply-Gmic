import krita

currentDoc = Krita.instance().activeDocument()
currentLayer = currentDoc.activeNode()
x = 0

while x <= 10:
          
    if currentLayer.hasKeyframeAtTime(currentDoc.currentTime()):
        Krita.instance().action('QMicAgain').trigger()
        Krita.instance().action('next_keyframe').trigger()
        
    else:
        break