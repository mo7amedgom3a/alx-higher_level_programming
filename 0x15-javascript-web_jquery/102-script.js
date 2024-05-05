$(document).ready(function () {
	$("INPUT#btn_translate").click(function () {
		const language_code = $("INPUT#language_code").val();
		$.getJSON(
			`https://hellosalut.stefanbohacek.dev/?lang=${language_code}`,
			function (data) {
				$("#hello").text(data.hello);
			}
		);
	});
});