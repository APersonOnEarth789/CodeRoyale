import { useState } from 'react';
import { Link, useNavigate } from "react-router-dom";
import { TextInput, PasswordInput, Button, Title, Paper, Text } from "@mantine/core";
// import errorPopup from "../../helpers/errorPopup";

import Header from "../../components/header.jsx";
import styles from "./styles/login.module.css";

const Login = () => {
  const [loginEmail, setLoginEmail] = useState("");
  const [loginPassword, setLoginPassword] = useState("");

  const navigate = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    navigate("/dashboard");
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