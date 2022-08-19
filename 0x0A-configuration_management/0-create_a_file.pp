# Init of the Puppet
file { '/tmp':
  path    => '/tmp/school'
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
    }
