# Puppet script to create ssh file
file { '/root/.ssh/config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
}

# Set IdentityFile to use the private key
file_line { 'Declare identity file':
  path  => '/root/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile',
}

# Disable password authentication
file_line { 'Turn off passwd auth':
  path  => '/root/.ssh/config',
  line  => '    PasswordAuthentication no',
  match => '^\s*PasswordAuthentication',
}
