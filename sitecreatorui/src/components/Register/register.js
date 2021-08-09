import React, {useState} from "react";
import {connect} from 'react-redux'

import {registerUser} from "../../redux/actions/authActionCreator";
import {Button} from "@material-ui/core";

import {toast} from "react-toastify";


const RegisterForm = ({dispatchRegisterAction}) => {

    const [firstname, setFirstName] = useState('');
    const [lastName, setLastName] = useState();
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();

    const handleOnSubmit = (event) =>{
        event.preventDefault();
        dispatchRegisterAction(firstname, lastName, email, password,
            () => toast.success("Account created Successfully!"),
            (message) => toast.error(`Error ${message}`));
    };


    return (
        <React.Fragment>
            <h2>New User?</h2>
            <h4>Create an account</h4>
            <br/>

            <form noValidate onSubmit={handleOnSubmit}>
                <div className="form-group">
                    <label htmlFor="firstName">First Name</label>
                    <input NoValidate id="firstName"
                           type='text'
                           name='firstName'
                           placeholder='First Name'
                           value={firstname}
                           onChange={(e) => setFirstName(e.target.value)}
                           className='form-control'
                    />
                </div>
                <div className="form-group">
                 <label htmlFor="firstName">Last Name</label>
                    <input NoValidate id="lastName"
                           type='text'
                           name='lastName'
                           placeholder='Last Name'
                           value={lastName}
                           onChange={(e) => setLastName(e.target.value)}
                           className='form-control'
                    />
                    </div>
                <div className="form-group">
                    <label htmlFor="email">Email Address</label>
                    <input NoValidate id="email"
                           type='email'
                           name='email'
                           placeholder='Email'
                           value={email}
                           onChange={(e) => setEmail(e.target.value)}
                           className='form-control'
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password1">Password</label>
                    <input NoValidate id="password1"
                           type='password'
                           name='password'
                           placeholder='password'
                           value={password}
                           onChange={(e) => setPassword(e.target.value)}
                           className='form-control'
                    />
                </div>

                <Button type='submit' className='btn btn-primary mr-2'>
                    Register| <i className="fas fa-user-plus"></i>
                </Button>

                <Button className='btn btn-outline-secondary'>
                    Cancel| <i className="fas fa-times"></i>
                </Button>




            </form>
        </React.Fragment>
    );
};

const mapDispatchToProps = dispatch => ({
    dispatchRegisterAction: (firstName, lastName, email, password, onSuccess,onError) =>
        dispatch(registerUser({firstName, lastName, email, password}, onSuccess, onError))

});

export default connect(null, mapDispatchToProps)(RegisterForm);
