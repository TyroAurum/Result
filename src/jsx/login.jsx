import React from 'react';
import { useEffect } from 'react';
import { useState } from 'react';
import {Link} from 'react-router-dom'
import {Form,FormGroup,Label,Input,Button} from 'reactstrap';
export var data = "";

const LoginCard = () => {
    const initialValues = {regno:"",dob:""};
    const [formValues,setFormvalues] = useState(initialValues);
    const [formErrors,setFormErrors] = useState();
    const [isSubmit,setIsSubmit] = useState(false);
    let noErr = "";
    let dobErr = "";

    const handleChange = (e) => {
        const {name,value} = e.target;
        setFormvalues({...formValues,[name]:value});
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        setFormErrors(validate(formValues));
        setIsSubmit(true);
        const Register = formValues.regno;
        const dob = formValues.dob;
        const API_URL = `https://resultvec.herokuapp.com/api/results/IT/`;
        const searchUser = async (Register,dob) => {
            const response = await fetch(`${API_URL}`);
            const information = await response.json();
            await for_loop();
            function for_loop(){
            for(let l=0;l<information.length;l++){
            if(Number(Register)===information[l].Register_No)
            {if(dob === information[l].DOB){
                data = information[l];
                document.getElementById("link_btn").click()
            }else{
                console.log(formErrors)
                dobErr = "Wrong Data";
                
            }
            }}

        }
        }

        searchUser(Register,dob);

        
    }

    useEffect(()=>{
        if ((formErrors && Object.keys(formErrors).length === 0) && isSubmit){
        };
    },[formErrors,formValues,isSubmit]);

    const validate = (values) => {
        const errors = {};
        //const regex = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
        if(!values.regno){
            errors.regno = "Register number required";
        }
        if(!values.dob){
            errors.dob = "Date of Birth required";
        }
        return errors;

    }

    return(<>
        <div className="containeer">
            <Form>
                <FormGroup>
                    <div className='input1'>
                    <Label>Register No.</Label>
                    <Input 
                    bsSize='lg'
                    type="text"
                    placeholder='Register Number'
                    name='regno'
                    value={formValues.regno}
                    onChange={handleChange}
                    /><span> {noErr}</span>
                    </div>
                    <br/><br/>
                    <div className='input2'>
                    <Label>Date of Birth</Label>
                    <Input
                    bsSize='lg'
                    type='date'
                    placeholder='Date of Birth'
                    name='dob'
                    value={formValues.dob}
                    onChange={handleChange}
                    />
                    </div><span> {dobErr}</span>
                    <br /><br />
                    <Button  onClick={handleSubmit}>Submit</Button>
                    <Link id='link_btn' to={{
                        pathname:"/results/IT",
                        state:data}}> </Link>
                </FormGroup>
            </Form>
      </div>
      </>
    );
}

export default LoginCard;
