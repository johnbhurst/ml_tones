
# 2023-06-04

* Calculate average, min, max durations for clips                    done
* Rename tabs to "00", "01", "02", etc.                              done
* Add "All" tab for summary of all voices                            done
* Rename split_audio.py to split_tones.py                            done
* Add option to omit chunks shorter than a min-duration              done
* Check actual durations of clips vs reported durations              done
* Check spectral analysis for some good and bad clips                done
* Investigate how to set up DVC for clip data                        done
* Record voices 11-19                                                done

# 2023-06-05

* Re-export Audacity projects with 32-bit float samples              done
* Program to analyze the min_duration parameter                      done
* Program to demonstrate JSON config file                            done
* Expand split_tones.py to support config file of parameters         done
* Redo spreadsheet of all clip data                                  done
* Install terraform                                                  done
* Create GCP project for ml_tones                                    done
* Create storage bucket for ml_tones                                 done

# 2023-06-10

* Separate split_tones to splitting tones and summary stats          done
* Push raw data to DVC                                               done
* DVC pipeline stage to generate tone clips for each voice           done
* DVC pipeline stage to generate summary stats and freq analysis     done
* DVC pipeline stage to generate waveform graphs for each clip       done

# 2023-06-11

* Fix bug in split_tones.py where not using min_duration             done
* Fix ordering in voice_stats CSV output                             done
* Change PNG image output to SVG                                     done
* What to do about ffmpeg requirement?                               done

# 2023-06-20

* DVC pipeline stage to generate HTML report?                        done

# 2023-07-02

* Any way to avoid Google API quota warnings?
