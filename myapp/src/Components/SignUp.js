import {useForm} from "react-hook-form";
import {useState} from "react";


function SignUp(){
    const {register, handleSubmit, errors} = useForm()
    const [userInfo, setUserInfo] = useState();

    const onSubmit = (data) => {
        setUserInfo(data);
        console.log(data);
    };
    console.log(errors);

    return(
        <div className='container'>
            <pre>{JSON.stringify(userInfo,undefined,2)}</pre>

            <form onSubmit={handleSubmit(onSubmit)}>
                <h1>Sign Up</h1>
                <div className="ui divider"></div>
                <div className="ui form">
                    <div className="field">
                        <label>Username</label>
                        <input type="text" name="username" placeholder="Username" ref={register({required:"Username is required"}) }/>
                    </div>
                    <p>{errors.email?.message}</p>
                    <div className="field">
                        <label>Email</label>
                        <input type="email" name="email" placeholder="Email" ref={register({required:"Email is required",pattern:{value:/^\s+@\s+$/i, message: "This is not a valid email",}}) }/>
                    </div>

                    <p>{errors.password?.message}</p>
                    <div className="field">
                        <label>Password</label>
                        <input type="password" name="password" placeholder="Password" ref={register({
                            required:"Password is required",
                            minLength: {
                                value: 4,
                                message: "Password",
                            },
                            maxLength:{
                                value: 10,
                                message: "Password cannot exceed more than 10 characters"
                            },

                        })}
                        />
                    </div>
                <div>
                    <p>{errors.username?.message}</p>
                    <button className='fluid ui button blue'>Submit</button>
                </div>
                </div>
                </form>
                </div>
    );
}

export default SignUp;