using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class control : MonoBehaviour
{
	public  float thrust;
	public  float torque;
	private  float timeWork;
	public  Rigidbody rb;
	public  GameObject Camera;
	public  float trot;
	public  float tсlose;
	public  float I;
	private float a;
	private float t;
	private int caseSwitch;
	private Vector3 vec, vectime;
	public  float M1;
	public  float M2;
	public  float f1;
	public  float f2;
	public  float C;


    // Start is called before the first frame update
    void Start()
    {   
    	rb = GetComponent<Rigidbody>();
        rb.inertiaTensor = new Vector3(I,I,I);
        a = thrust/rb.mass;
        caseSwitch  = 1;
        //Time.timeScale = 10.0f;
    }
    
    // Update is called once per frame capsule
    void FixedUpdate(){   
    	if (Input.GetKey("left"))   rb.AddForce(transform.right * (-4), ForceMode.Force); 
	    if (Input.GetKey("right"))  rb.AddForce(transform.right * (4), ForceMode.Force); 

      	switch (caseSwitch){
      		case 1:
	        	if (Input.GetKey("q")) 
	        		caseSwitch = 2;
	        		timeWork = 0;//Time.time;
	          	break;
	        case 2:
	        	vec = Fun1();
	        	if (vec.y != 0){ 
	        		caseSwitch = 3;
	        		timeWork = Time.deltaTime;
	        	}
	        	else 
	        		caseSwitch = 5;
	          	break;
	        case 3:
	        	vectime = Fun2(vec.y);
	        	caseSwitch = 4;
	        	break;
	        case 4:
	        	if (Fun3(vectime)){
	        		caseSwitch = 5;
	        	}
	        	break;
	        case 5:
	        	timeWork = 0;
	        	vectime = Fun4(vec);
	        	caseSwitch = 6;
	        	break;
	        case 6:
	        	Fun5(vectime);
	        	break;
	        default:
	            Debug.Log("default");
	            break;
        }
   }

    Vector3 Fun1(){ // расстояние и угол
   		Vector3 fwd = Camera.transform.TransformDirection(Vector3.forward);
   		Ray ray = new Ray(Camera.transform.position, fwd);
   		Debug.DrawRay(ray.origin, ray.direction * 20f, Color.red, 20);
   		if (Physics.Raycast(ray, out RaycastHit hit)){
        	return new Vector3(hit.distance, Camera.transform.localRotation.eulerAngles.y, 0);
        }
        return new Vector3(0,0,0);
   }

    Vector3 Fun2(float ang){ //время поворота
		ang = Mathf.Deg2Rad * ang; //перевод в радианы
    	if (ang > 3.14f) ang = 3.14f - ang;	
        if (ang < 0) 
        	t = trot/2 - Mathf.Sqrt(trot*trot/4 + ang*I/torque);
        else 
        	t = trot/2 - Mathf.Sqrt(trot*trot/4 - ang*I/torque);
        float tmed = t;
        float tend = trot; 
        return new Vector3(tmed, tend, 0);	
    }

    bool Fun3(Vector3 vt){ //поворот
    	float tmed = vt.x;
    	float tend = vt.y;
    	timeWork += Time.deltaTime;
    	if (timeWork < tend){
        	if (timeWork < tmed){
        		rb.AddTorque(transform.up * (torque + M1), ForceMode.Force); 
        		//Debug.Log(string.Format("timeWork: {0}, tend: {1}, tmed: {2}, Force: {3}", timeWork, tend, tmed, -torque));
        	}
        	else if(timeWork > tend - tmed){
        		rb.AddTorque(transform.up * (- torque + M2), ForceMode.Force);
        		//Debug.Log(string.Format("timeWork: {0}, tend: {1}, tmed: {2}, Force: {3}", timeWork, tend, tmed, torque));
        	}
        	return false;
        } 
        else {
        	return true;
        }

    }

    Vector3 Fun4(Vector3 xyz){ //время сближения    	
		float S = xyz.x; 
		//Debug.Log("S = " + S);
		//Debug.Log((tсlose*tсlose/4 - S*rb.mass/thrust));
        t = tсlose/2 - Mathf.Sqrt(tсlose*tсlose/4 - S*rb.mass/thrust);
        //tmin = tсlose/2 - Mathf.Sqrt(tсlose*tсlose/4 - S*I/torque);
        //tmax = tсlose/2 + Mathf.Sqrt(tсlose*tсlose/4 - S*I/torque);
        float tmed = t;     
        float tend = tсlose;  
		//Debug.Log("tmed = " + tmed);
		//Debug.Log("tend = " + tend);

        return new Vector3(tmed, tend, 0);	
    }

 //вперед 
    bool Fun5(Vector3 vt){
        float tmed = vt.x;
        float tend = vt.y; 
        timeWork += Time.deltaTime;
        if (timeWork < tend){
        	if (timeWork < tmed){
        		//Debug.Log(string.Format("1timeWork: {0}, tend: {1}, tmed: {2}, Force: {3}", timeWork, tend, tmed, thrust));
        		rb.AddForce(transform.forward * (thrust + f1), ForceMode.Force); 
        		//rb.AddForce(transform.right * (-4), ForceMode.Force); 
        		
        	}
        	else if(timeWork > tend - tmed){
        		//Debug.Log(string.Format("2timeWork: {0}, tend: {1}, tmed: {2}, Force: {3}", timeWork, tend, tmed, -thrust));
        		rb.AddForce(transform.forward * ( - thrust + f2), ForceMode.Force);
        		//rb.AddForce(transform.right * (-4), ForceMode.Force); 
        		
        	}
        	else{
        		Debug.Log("0");
        	}
        	return false;
        } 
        else {
        	C = 100 * (0.5842284f) / Mathf.Sqrt(Mathf.Pow((0.5842284f), 2) + Mathf.Pow((rb.position.z), 2));
        	Time.timeScale = 0.0f;
        	return true;
        }
    }


   /*void Fun2(){
   		Debug.Log("Fun2");
   		Quaternion r1 = Camera.transform.localRotation;
   		Debug.Log(r1.eulerAngles);
   		Quaternion r2 = Camera.transform.rotation;
   		Debug.Log(r2.eulerAngles);
   		Debug.Log(r1.eulerAngles - r2.eulerAngles);
   		transform.Rotate(r1.eulerAngles - r2.eulerAngles);


   		//Debug.Log(Camera.transform.localRotation);
   		//Debug.Log(Camera.localRotation);
   		//Debug.Log(Camera.transform.rotation);
   		//transform.rotation = Quaternion.Slerp(from.rotation, to.rotation, timeCount);
   		//transform.Rotate(Camera.transform.localRotation + Camera.transform.rotation);
   		//Debug.Log(Rotation);
   		//respawns = GameObject.FindGameObjectsWithTag("CameraRig");

   }*/









   /*
    	if (Input.GetKey("q")){
    		rb.angularDrag = 1.0F;
	        if (Input.GetKey("up"))     rb.AddTorque(transform.right * (-thrust),ForceMode.Force);
	        if (Input.GetKey("down"))   rb.AddTorque(transform.right * thrust,ForceMode.Force);

	        if (Input.GetKey("left"))   rb.AddTorque(transform.up * (-thrust),ForceMode.Force);
	        if (Input.GetKey("right"))  rb.AddTorque(transform.up * thrust,ForceMode.Force);
	        
	        if (Input.GetKey("w"))      rb.AddTorque(transform.forward * thrust,ForceMode.Force);
	        if (Input.GetKey("s"))      rb.AddTorque(transform.forward * (-thrust),ForceMode.Force);
		}
		else{
			rb.angularDrag = 3.0F;
			if (Input.GetKey("up"))     rb.AddForce(transform.up *        thrust,   ForceMode.Force);
	        if (Input.GetKey("down"))   rb.AddForce(transform.up *      (-thrust),  ForceMode.Force);
	        if (Input.GetKey("left"))   rb.AddForce(transform.right *   (-thrust),  ForceMode.Force);
	        if (Input.GetKey("right"))  rb.AddForce(transform.right *     thrust,   ForceMode.Force);
	        if (Input.GetKey("w"))      rb.AddForce(transform.forward *   thrust,   ForceMode.Force);
	        if (Input.GetKey("s"))      rb.AddForce(transform.forward *  (-thrust), ForceMode.Force);     
		};

		if (Input.GetKeyDown("z"))	{
			timeStart = Time.time + timeWork;
			timeEnd = Time.time + 2 * timeWork;
		};

		t = Time.time - timeStart; 

		if (timeStart > 0){
			if (Time.time < timeStart){
				rb.AddForce(transform.forward * F, ForceMode.Force);
				S = a*t*t/2;
			}
			if (Time.time > timeStart){
				if (Time.time < timeEnd){
					rb.AddForce(transform.forward * (-F), ForceMode.Force);
					S = a*t - a*t*t/2;
					// Debug.Log("2");
					// S += F/rb.mass*timeWork*timeWork/2;
				}
			}
		}
    }

    void Find(){
    	Vector3 fwd = transform.TransformDirection(Vector3.forward);
        if (Physics.Raycast(transform.position, fwd, 10))
            Debug.Log("There is something in front of the object!");

    }
*/
}
