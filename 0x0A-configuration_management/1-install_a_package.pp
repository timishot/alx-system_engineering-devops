# 1-install_a_package.pp

package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin:/bin',
  refreshonly => true,
}

# Notify when the installation is complete
notify { 'Flask installed successfully':
  subscribe => Exec['install_flask'],
}

