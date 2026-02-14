import React from "react";

const Footer = () => {
  return (
    <footer className="custom-footer">
      <div className="container">
        <div className="footer-logo">
          <img src="/assets/logo.png" alt="University Logo" height="70" />
        </div>

        <div className="footer-links">
          <a href="/about">درباره ما</a>
          <a href="/contact">تماس با ما</a>
          <a href="/privacy">حریم خصوصی</a>
          <a href="/terms">قوانین استفاده</a>
        </div>

        <div className="footer-copy">
          © 2026 سامانه آموزش الکترونیکی
        </div>
      </div>
    </footer>
  );
};

export default Footer;
