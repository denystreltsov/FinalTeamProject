#include "libdeniaudio.h"


int main(int argc, char const *argv[])
{
    AudioInit();


    MixingTwoAudio("/Users/deni/Desktop/music3.flac", "/Users/deni/Desktop/music4.flac");

    PlayAudio();

    AudioEnd();


    return 0;
}
