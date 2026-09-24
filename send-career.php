<?php
// send-career.php - PHP Backend Script for Dealex Career Form Submissions
header('Content-Type: application/json');

// Configuration
$to_email = "hr@dealex.pk";
$subject_prefix = "Job Application:";

// Enable error reporting for debugging if needed, but output JSON only
error_reporting(0);
ini_set('display_errors', 0);

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'message' => 'Invalid request method.']);
    exit;
}

// Retrieve & sanitize form data
$name     = isset($_POST['applicant_name']) ? trim(filter_var($_POST['applicant_name'], FILTER_SANITIZE_STRING)) : '';
$email    = isset($_POST['applicant_email']) ? trim(filter_var($_POST['applicant_email'], FILTER_SANITIZE_EMAIL)) : '';
$phone    = isset($_POST['applicant_phone']) ? trim(filter_var($_POST['applicant_phone'], FILTER_SANITIZE_STRING)) : '';
$position = isset($_POST['applicant_position']) ? trim(filter_var($_POST['applicant_position'], FILTER_SANITIZE_STRING)) : '';
$message  = isset($_POST['applicant_message']) ? trim(filter_var($_POST['applicant_message'], FILTER_SANITIZE_STRING)) : '';

// Validation
if (empty($name) || empty($email) || empty($phone) || empty($position) || empty($message)) {
    echo json_encode(['success' => false, 'message' => 'Please fill in all required fields.']);
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo json_encode(['success' => false, 'message' => 'Invalid email address provided.']);
    exit;
}

// Handle CV File Attachment
$has_attachment = false;
$file_tmp  = '';
$file_name = '';
$file_type = '';
$file_size = 0;

if (isset($_FILES['cv_file']) && $_FILES['cv_file']['error'] === UPLOAD_ERR_OK) {
    $file_tmp  = $_FILES['cv_file']['tmp_name'];
    $file_name = basename($_FILES['cv_file']['name']);
    $file_size = $_FILES['cv_file']['size'];
    $file_ext  = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));

    $allowed_extensions = ['pdf', 'doc', 'docx'];
    if (!in_array($file_ext, $allowed_extensions)) {
        echo json_encode(['success' => false, 'message' => 'Invalid file format. Only PDF, DOC, and DOCX files are allowed.']);
        exit;
    }

    if ($file_size > 10 * 1024 * 1024) { // 10MB limit
        echo json_encode(['success' => false, 'message' => 'Uploaded file exceeds the maximum limit of 10MB.']);
        exit;
    }

    $has_attachment = true;
    $file_type = mime_content_type($file_tmp);
} else {
    echo json_encode(['success' => false, 'message' => 'Please attach your CV / Resume file.']);
    exit;
}

// Construct Email Subject & Body
$email_subject = "$subject_prefix $name - $position";

// Boundary for multipart email
$semi_rand = md5(time());
$mime_boundary = "==Multipart_Boundary_x{$semi_rand}x";

// Headers
$headers  = "From: Dealex Careers <no-reply@dealex.pk>\r\n";
$headers .= "Reply-To: $name <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: multipart/mixed;\r\n boundary=\"{$mime_boundary}\"";

// Plain text body content
$body_content = "Candidate Application Details:\n\n";
$body_content .= "Full Name: " . $name . "\n";
$body_content .= "Email: " . $email . "\n";
$body_content .= "Phone: " . $phone . "\n";
$body_content .= "Position Applied For: " . $position . "\n";
$body_content .= "Attached File: " . $file_name . "\n\n";
$body_content .= "Cover Note / Message:\n" . $message . "\n\n";
$body_content .= "--- Sent from Dealex Careers Page ---";

// Email Multipart Body
$message_body  = "--{$mime_boundary}\r\n";
$message_body .= "Content-Type: text/plain; charset=\"UTF-8\"\r\n";
$message_body .= "Content-Transfer-Encoding: 7bit\r\n\r\n";
$message_body .= $body_content . "\r\n\r\n";

// Add Attachment
if ($has_attachment && file_exists($file_tmp)) {
    $file_data = file_get_contents($file_tmp);
    $file_encoded = chunk_split(base64_encode($file_data));

    $message_body .= "--{$mime_boundary}\r\n";
    $message_body .= "Content-Type: {$file_type}; name=\"{$file_name}\"\r\n";
    $message_body .= "Content-Description: {$file_name}\r\n";
    $message_body .= "Content-Disposition: attachment;\r\n filename=\"{$file_name}\"; size={$file_size};\r\n";
    $message_body .= "Content-Transfer-Encoding: base64\r\n\r\n";
    $message_body .= $file_encoded . "\r\n\r\n";
}

$message_body .= "--{$mime_boundary}--";

// Send Email via PHP mail()
$mail_success = @mail($to_email, $email_subject, $message_body, $headers);

if ($mail_success) {
    echo json_encode(['success' => true, 'message' => 'Your application and CV have been sent successfully to HR at hr@dealex.pk!']);
} else {
    echo json_encode(['success' => false, 'message' => 'Failed to send email. Please ensure mail service is configured on your server or contact hr@dealex.pk directly.']);
}
?>
