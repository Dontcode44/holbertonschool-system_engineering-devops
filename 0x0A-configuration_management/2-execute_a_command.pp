# Pkill
exec {'killmenow':
command  => 'pkill',
provider => 'excec'
}
