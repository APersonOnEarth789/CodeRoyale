import styles from "./styles/header.module.css";
import { Link, useNavigate } from "react-router-dom";
import profile from "../assets/account.png"

const Header = ({ isLoggedIn }) => {
  const navigate = useNavigate();

  return (
    <div className={styles["bar"]}>
      <img src={profile} alt="profile" className={styles["profile"]} />
      <div className={styles["name"]} onClick={() => navigate("/")}>Code Royale</div>
      {/* <Link to="/stats" className={styles["stats-big"]}>Statistics</Link>
      <Link to="/stats" className={styles["stats-small"]}>Stats</Link> */}
      {!isLoggedIn && <button className={styles["log"]} onClick={() => navigate("/login")}>Login</button>}
      {isLoggedIn && <button className={styles["log"]} onClick={() => navigate("/")}>Logout</button>}
    </div>
  );
}

export default Header;