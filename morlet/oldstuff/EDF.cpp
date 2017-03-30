#include <iostream>
#include <algorithm>


class EDF {


};



EDF::read_header(auto &fstream) {

}

auto EDF::read_hdr_preamble(auto &fstream) {
  char version[8];
  char patientID[80];
  char record_info[80];
  char startdate[8];
  char starttime[8];
  char hdrbytes[8];
  char reserved[44];
  char NR[8];
  char rec_dur[8];
  char NS[4];
  version << fstream;
  patientID << fstream;
  record_info << fstream;
  startdate << fstream;
  hdrbytes << fstream;
  reserved << fstream;
  NR << fstream;
  rec_dur << fstream;
  NS << fstream;
  


}
