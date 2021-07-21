import Navbar from './Components/Navbar';
import Profile from './Components/Profile';
import Header from "./Components/Header";
import Footer from "./Components/Footer";
import Login from "./Components/Login";


const App =() => {
    return(
        <div className='app-wrapper'>
            <Login/>
            <Header/>
            <Navbar/>
            <Profile/>
            <Footer/>

        </div>

    )

}

export default App