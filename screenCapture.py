import definitions
from util import connectionAdaptor, getActivityPackage, safeScreenshot, saveXmlScreen


def screenCap(
    phoneDevice=definitions.PHONE_SERIAL,
    tabletDevice=definitions.TABLET_SERIAL,
    saveDir=definitions.OUT_DIR,
):
    d1, d2, connectStatus = connectionAdaptor(phoneDevice, tabletDevice)
    while not connectStatus:
        d1, d2, connectStatus = connectionAdaptor(phoneDevice, tabletDevice)

    d1_activity, d1_package, d1_launcher = getActivityPackage(d1)
    d2_activity, d2_package, d2_launcher = getActivityPackage(d2)

    xml1 = d1.dump_hierarchy(compressed=True)
    xml2 = d2.dump_hierarchy(compressed=True)
    img1 = safeScreenshot(d1)
    img2 = safeScreenshot(d2)

    saveXmlScreen(saveDir, xml1, xml2, img1, img2, d1_activity, d1_package)


if __name__ == "__main__":
    screenCap()
