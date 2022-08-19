# Init of the Puppet

class filetest {
file { '/tmp':
  path    => '/tmp/school'
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
    }
}
