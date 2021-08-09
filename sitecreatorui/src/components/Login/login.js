import React, {useState} from "react";
import {Button} from "@material-ui/core";
import {toast} from "react-toastify";
import {connect} from "react-redux";
import {loginUser} from "../../redux/actions/authActionCreator";
import mapDispatchToProps from "react-redux/lib/connect/mapDispatchToProps";


const LoginForm = ({dispatchLoginAction}) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('')

    const handleOnSubmit = (event) => {
        event.preventDefault();
        dispatchLoginAction(email, password,
            () => toast.success("Logged in successfully"),
            (message) => toast.error(`Error: ${message}`));

    };




    return (
        <React.Fragment>
            <h2>Have an Account?</h2>
            <h4>Login here</h4>
            <br/>

            <form noValidate onSubmit={handleOnSubmit}>
                <div className="form-group">
                <label htmlFor="email">Email Address</label>
                <input noValidate id="email"
                       type="email"
                       name="email"
                       placeholder="Email"
                       value={email}
                       onChange={(e) => setEmail(e.target.value)}
                       className="form-control"
                />
                </div>

                <div className="form-group">
                <label htmlFor="email">Password</label>
                <input noValidate id="password"
                       type="password"
                       name="password"
                       placeholder="Password"
                       value={password}
                       onChange={(e) => setPassword(e.target.value)}
                       className="form-control"
                />
                </div>

                <Button type="submit" className="btn btn-primary mr-2">
                    Login | <i className="fas fa-sign-in-alt"></i>
                </Button>
                <Button type="submit" className="btn btn-outline-secondary">
                    Cancel | <i className="fas fa-times"></i>
                </Button>

            </form>
        </React.Fragment>
    );
};

export default connect(null, mapDispatchToProps)(LoginForm);
