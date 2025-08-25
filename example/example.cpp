#include "zimmergripper.h"

int main(){
    ZimmerGripper *gthis;
    gthis = SetGripper();
    Connect(gthis, "192.168.137.254", 502);
    Init(gthis);
    Grip(gthis);
    Release(gthis);
    Disconnect(gthis);

    return 0;
}