$file_to_edit = '/var/www/html/wp-settings.php'

exec { fix-wordpress':
	command => "sed -i 's/phpp/php/g' ${file_to_edit}",
	path    => ['/bin','/usr/bin']
}
