# Increases the traffic the Nginx server can handle

# Increase the limit of the default file
exec { 'fix-for-ngix':
  # Change the limit value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Specify path to be changed
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
