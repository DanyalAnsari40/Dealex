<?php
// send-contact.php - PHP Backend Script for Dealex Contact Form Submissions
header('Content-Type: application/json');

// Recipient Email Configuration
$to_email = "logistics@dealex.pk";
$subject_prefix = "Website Contact Inquiry:";

// Disable direct error output to preserve clean JSON responses
error_reporting(0);
ini_set('display_errors', 0);

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'message' => 'Invalid request method.']);
    exit;
}

// Retrieve & sanitize form data
$first_name = isset($_POST['first_name']) ? trim(strip_tags($_POST['first_name'])) : '';
$last_name  = isset($_POST['last_name']) ? trim(strip_tags($_POST['last_name'])) : '';
$email      = isset($_POST['email']) ? trim(filter_var($_POST['email'], FILTER_SANITIZE_EMAIL)) : '';
$message    = isset($_POST['message']) ? trim(strip_tags($_POST['message'])) : '';

$full_name = trim($first_name . ' ' . $last_name);

// Validation
if (empty($first_name) || empty($email) || empty($message)) {
    echo json_encode(['success' => false, 'message' => 'Please fill in all required fields (First Name, Email, and Message).']);
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo json_encode(['success' => false, 'message' => 'Please provide a valid email address.']);
    exit;
}

// Construct Email Subject & Headers
$email_subject = "$subject_prefix $full_name";

$headers  = "From: Dealex Contact Form <no-reply@dealex.pk>\r\n";
$headers .= "Reply-To: $full_name <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

// Email Body Content
$body_content  = "New Contact Form Inquiry Details:\n\n";
$body_content .= "Full Name: " . $full_name . "\n";
$body_content .= "Email: " . $email . "\n\n";
$body_content .= "Message:\n" . $message . "\n\n";
$body_content .= "--- Sent from Dealex Contact Us Page ---";

// Send Email via PHP mail()
$mail_success = @mail($to_email, $email_subject, $body_content, $headers);

if ($mail_success) {
    echo json_encode([
        'success' => true,
        'message' => 'Thank you! Your message has been sent successfully to logistics@dealex.pk.'
    ]);
} else {
    echo json_encode([
        'success' => false,
        'message' => 'Failed to send message via mail service. Please contact us directly at logistics@dealex.pk.'
    ]);
}
?>
