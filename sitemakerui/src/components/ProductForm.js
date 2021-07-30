import React from "react";
import {Typography} from "@material-ui/core";

export const ProductForm = () => {
    return(

        <Typography variant="h2" align="center" color="textPrimary" gutterBottom>Welcome to SiteMaker!
                <h2>It's time to create!</h2>
                <h3>Create product!</h3>

        <form>
            <div className="form-group">
               <ul>
                <input
                    type ='text'
                    className='form-control'
                    placeholder='Enter the productname'
                />
               </ul>

                <ul>

                    <input
                    type ='text'
                    className='form-control'
                    placeholder='Enter the price'
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
                    placeholder='Enter the storename'
                />

                </ul>


            </div>
        </form>
    </Typography>
    )
}