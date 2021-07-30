import React from "react";
import {Typography} from "@material-ui/core";

export const ShopForm = () => {
    return(

        <Typography variant="h2" align="center" color="textPrimary" gutterBottom>Welcome to SiteMaker!
                <h2>It's time to create!</h2>
                <h3> Create shop! </h3>

        <form>
            <div className="form-group">
               <ul>
                <input
                    type ='text'
                    className='form-control'
                    placeholder='Enter the name of store'
                />
               </ul>

                <ul>

                    <input
                    type ='text'
                    className='form-control'
                    placeholder='Enter the description'
                />

                </ul>

                <ul>

                    <input
                    type ='text'
                    className='form-control'
                    placeholder='Enter the owner'
                />

                </ul>

            </div>
        </form>
    </Typography>
    )
}