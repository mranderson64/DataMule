<?php 
$protocol = stripos($_SERVER['SERVER_PROTOCOL'],'https') === 0 ? 'https://' : 'http://';
$host = $protocol . $_SERVER['HTTP_HOST'];
$urip = $_SERVER['REQUEST_URI'];
$uri = str_replace("/", "-", $urip); 
#$urib = str_replace("/liam", "", $urip); // liams stupid dev enviroment
#$uri = str_replace("/", "-", $urib); 
if($uri == "" || $uri == "-"){
	$uri = "home";
}
$xml = simplexml_load_file("./XML/" . $uri . ".xml") or die("Error: Cannot create object");
$title = $xml->title;
$description = $xml->description;
$useTemplate = $xml->useTemplate;
$template = $xml->template;
$usehtml = $xml->usehtml;
$contentTitle = $xml->contentTitle;
$content = $xml->content;
if($useTemplate == "true"){
	include "./templates/" . $template . ".php";
	$parseOutput = $templateOutput;
}else if($usehtml == "true"){
	$parseOutput = '<div class="container">' . $content . '</div>';
}
?>