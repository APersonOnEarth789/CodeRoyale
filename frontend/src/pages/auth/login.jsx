import { useState } from 'react';
import { Link, useNavigate } from "react-router-dom";
import { TextInput, PasswordInput, Button, Title, Paper, Text } from "@mantine/core";
// import errorPopup from "../../helpers/errorPopup";

import Header from "../../components/header.jsx";
import styles from "./styles/login.module.css";


const Login = () => {
  const [loginEmail, setLoginEmail] = useState("");
  const [loginPassword, setLoginPassword] = useState("");
  const [error, setError] = useState("");

  const navigate = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/auth/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({"password": loginPassword, "username": loginEmail}) // could be problematic
      });

      const text = await response.text();
      // console.log("RAW RESPONSE:", text);

      let data;
      try {
        data = JSON.parse(text); // try parsing JSON
      } catch {
        data = null; // not JSON (HTML case)
      }

      if (response.ok) {
        // const data = await response.json();
        localStorage.setItem("USER_TOKEN", data.access_token);
        navigate("/dashboard");
      } else {
        // const errorData = await response.json();
        // console.log(errorData);
        // let message = errorData.validation_error.body_params[0].msg || "Unknown Login Error";

        let message =
          data?.message ||
          data?.detail ||
          data?.error ||
          data?.validation_error.body_params[0].msg ||
          "Login failed";
        
        // fallback: extract from HTML
        if (!data && text.includes("<p>")) {
          const match = text.match(/<p>(.*?)<\/p>/);
          if (match) message = match[1];
        }

        // console.log(message);
        setError(message);
      }
    } catch (error) {
      console.log(e);
    }
  };

  const toLandingPage = (e) => {
    e.preventDefault();
    navigate("/");
  };


  return (
    <>
      <Header />

      <div className={styles["page"]}>
        <Paper
          shadow="lg"
          radius="md"
          p="xl"
          withBorder
          mx="auto"
          style={{ maxWidth: 400, margin: "40px auto", marginTop: "120px", textAlign: "center" }}
        >
          <Title order={2} mb="md">Login</Title>

          <form onSubmit={submit}>
            <TextInput
              label="Email"
              placeholder="email@example.com"
              value={loginEmail}
              onChange={(e) => setLoginEmail(e.target.value)}
              required
              mb="sm"
              classNames={{ input: 'input' }}
              data-testid="login-email"
            />

            <PasswordInput
              label="Password"
              placeholder="Your Password"
              value={loginPassword}
              onChange={(e) => setLoginPassword(e.target.value)}
              required
              mb="md"
              classNames={{ input: 'input' }}
              data-testid="login-password"
            />
            
            {error && <Text fz="sm" color="red" mb="15px">{error}</Text>}

            <Button type="submit" className={styles["submit-button"]}>
              Login
            </Button>
          </form>

          <Text size="sm" mt="md" mb="xl">
            Don’t have an account?{" "}
            <Link to="/register" className={styles["login-button"]}>
              Register
            </Link>
          </Text>

          <a href="/" className={styles["back-to-landing-page"]}>To landing page</a>
        </Paper>
      </div>
    </>
  );
}

export default Login;