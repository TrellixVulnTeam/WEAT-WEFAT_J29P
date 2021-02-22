/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 4.0.1
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.deepspeech.libdeepspeech;

/**
 * Stores text of an individual token, along with its timing information
 */
public class TokenMetadata {
  private transient long swigCPtr;
  protected transient boolean swigCMemOwn;

  protected TokenMetadata(long cPtr, boolean cMemoryOwn) {
    swigCMemOwn = cMemoryOwn;
    swigCPtr = cPtr;
  }

  protected static long getCPtr(TokenMetadata obj) {
    return (obj == null) ? 0 : obj.swigCPtr;
  }

  public synchronized void delete() {
    if (swigCPtr != 0) {
      if (swigCMemOwn) {
        swigCMemOwn = false;
        throw new UnsupportedOperationException("C++ destructor does not have public access");
      }
      swigCPtr = 0;
    }
  }

  /**
   *  The text corresponding to this token 
   */
  public String getText() {
    return implJNI.TokenMetadata_Text_get(swigCPtr, this);
  }

  /**
   *  Position of the token in units of 20ms 
   */
  public long getTimestep() {
    return implJNI.TokenMetadata_Timestep_get(swigCPtr, this);
  }

  /**
   *  Position of the token in seconds 
   */
  public float getStartTime() {
    return implJNI.TokenMetadata_StartTime_get(swigCPtr, this);
  }

}
